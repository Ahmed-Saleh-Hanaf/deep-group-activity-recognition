# The Dataset class is responsible for:
#   1- knowing the dataset structure on the disk.
#   2- Mapping index to sample
#   3- Loading only what config requests 
#   4- Appling augmentation according to the transform function

import os
from typing import List, Dict, Any, Optional

from torch.utils.data import Dataset
from torchvision.io import read_image


MODES = {"image", "persons", "clip", "clip_persons"}

class VolleyballDataset(Dataset):
    """
    PyTorch Dataset for the Volleyball Group Activity Recognition dataset.

    This dataset supports multiple loading modes for different model types:
        - "image": Single target frame with group activity label
        - "persons": Cropped persons from target frame with individual + group labels
        - "clip": Sequence of frames with group activity
        - "clip_persons": Persons across frames in a clip with activities

    Args:
        root_dir (str):
            Path to dataset root directory. Expected structure:
                root_dir/
                    vid_id/
                        clip_id/
                            frame.jpg
                        annotations.txt

        vid_ids (List[int]):
            List of video IDs to include.

        mode (str):
            Data loading mode. Must be one of:
                ["image", "persons", "clip", "clip_persons"]

        transform (callable, optional):
            Optional transform applied to loaded images or clip.

    Raises:
        ValueError:
            If mode is invalid or vid_ids is empty.

        FileNotFoundError:
            If root directory or video folders are missing.
    """

    def __init__(
        self,
        root_dir: str,
        vid_ids: List[int],
        mode: str,
        transform: Optional[Any] = None,
    ):
        super().__init__()

        # ---------- Validation ----------
        if not os.path.exists(root_dir):
            raise FileNotFoundError(f"Dataset root not found: {root_dir}")

        if len(vid_ids) == 0:
            raise ValueError("vid_ids list cannot be empty")

        if mode not in MODES:
            raise ValueError(
                f"Invalid mode '{mode}'. Supported modes: {MODES}"
            )

        # ---------- Attributes ----------
        self.root_dir = root_dir
        self.mode = mode
        self.transform = transform

        self.clips: List[Dict[str, Any]] = []                       # [{"vid_id": num, "clip_id": num, "frames": []}]
        self.vid_imgs: Dict[int, Dict[int, Dict[str, Any]]] = {}    # { vid_id: {img_id: {"img_path": "path", "img_ann": "ann"}}}

        # ---------- Load metadata ----------
        self._load_metadata(vid_ids)

        if len(self.clips) == 0:
            raise RuntimeError("No clips found. Check dataset structure.")

    # =========================================================
    # Metadata Loading
    # =========================================================

    def _load_metadata(self, vid_ids: List[int]) -> None:
        """Load dataset structure and annotations into memory."""

        for vid_id in vid_ids:
            vid_path = os.path.join(self.root_dir, str(vid_id))

            if not os.path.isdir(vid_path):
                raise FileNotFoundError(
                    f"Video folder not found: {vid_path}"
                )

            self.vid_imgs[vid_id] = {}

            # ---------- Read Clips ----------
            for clip_id in os.listdir(vid_path):
                if clip_id == "annotations.txt":
                    continue

                clip_path = os.path.join(vid_path, clip_id)
                if not os.path.isdir(clip_path):
                    raise FileNotFoundError(
                    f"Clip folder not found: {clip_path}"
                )

                frame_ids = []

                for img_file in os.listdir(clip_path):
                    img_path = os.path.join(clip_path, img_file)

                    if not os.path.isfile(img_path):
                        continue

                    img_id = int(os.path.splitext(img_file)[0])

                    self.vid_imgs[vid_id][img_id] = {
                        "img_path": img_path
                    }

                    frame_ids.append(img_id)

                self.clips.append(
                    {
                        "vid_id": vid_id,
                        "clip_id": int(clip_id),
                        "frames": sorted(frame_ids),
                    }
                )

            # ---------- Read Annotations ----------
            ann_file = os.path.join(vid_path, "annotations.txt")

            if os.path.exists(ann_file):
                with open(ann_file, "r") as f:
                    for line in f:
                        if not line.strip():
                            continue

                        img_id = int(os.path.splitext(line.strip())[0])

                        if img_id in self.vid_imgs[vid_id]:
                            self.vid_imgs[vid_id][img_id]["ann"] = (
                                line.strip()
                            )

    # =========================================================
    # Required Dataset Methods
    # =========================================================

    def __len__(self) -> int:
        return len(self.clips)

    def __getitem__(self, index: int):
        if index < 0 or index >= len(self.clips):
            raise IndexError("Dataset index out of range")

        if self.mode == "image":
            return self._get_image_item(index)

        elif self.mode == "clip":
            return self._get_clip_item(index)

        elif self.mode == "persons":
            return self._get_person_item(index)

        elif self.mode == "clip_persons":
            return self._get_clip_persons_item(index)

        raise RuntimeError("Invalid mode — should never reach here")

    # =========================================================
    # Mode Implementations
    # =========================================================

    def _get_image_item(self, index: int):
        """
        Returns:
            image: Tensor [C, H, W]
            group_activity: int
        """

        clip = self.clips[index]
        vid_id = clip["vid_id"]

        target_frame = clip["clip_id"]

        metadata = self.vid_imgs[vid_id][target_frame]

        if metadata is None:
            raise KeyError(f"No metadata for frame {target_frame}")

        if "ann" not in metadata:
            raise KeyError(f"No annotation for frame {target_frame}")

        img_path = metadata["img_path"]
        annotation = metadata["ann"]

        img = read_image(img_path)

        if self.transform:
            img = self.transform(img)

        group_activity = annotation.split()[1]

        return img, group_activity

    # -------- Placeholder methods (to implement later) --------

    def _get_clip_item(self, index):
        raise NotImplementedError("clip mode not implemented yet")

    def _get_person_item(self, index):
        raise NotImplementedError("persons mode not implemented yet")

    def _get_clip_persons_item(self, index):
        raise NotImplementedError("clip_persons mode not implemented yet")
