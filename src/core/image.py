from fastapi import UploadFile

from src.core.cloudinary import (
  delete_image as cloudinary_delete_image,
  extract_public_id,
  upload_image_1_1 as cloudinary_upload_1_1,
  upload_image_16_9 as cloudinary_upload_16_9,
)


def upload_image_1_1(path: str, file: UploadFile) -> str:
  public_id = None
  try:
    url, public_id = cloudinary_upload_1_1(file_bytes=file.file.read(), folder=path)
    return url
  except Exception as e:
    if public_id:
      try:
        cloudinary_delete_image(public_id)
      except Exception:
        pass
    raise e


def upload_image_16_9(path: str, file: UploadFile) -> str:
  public_id = None
  try:
    url, public_id = cloudinary_upload_16_9(file_bytes=file.file.read(), folder=path)
    return url
  except Exception as e:
    if public_id:
      try:
        cloudinary_delete_image(public_id)
      except Exception:
        pass
    raise e


def delete_image_by_url(url: str) -> bool:
  try:
    public_id = extract_public_id(url)
    if public_id:
      cloudinary_delete_image(public_id)
    return True
  except Exception:
    return False
