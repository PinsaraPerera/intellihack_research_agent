import os
from google.cloud import storage
from logging_config import logger


def download_from_gcp(bucket_name, source_folder_path, local_dest_path):
    """
    Download files from a Google Cloud Storage bucket to a local directory.

    :param bucket_name: The name of the GCS bucket.
    :param source_folder_path: The path to the folder in the bucket to download files from.
    :param local_dest_path: The local directory to download files to.
    """
    client = storage.Client()

    try:
        bucket = client.bucket(bucket_name)
        blobs = bucket.list_blobs(prefix=source_folder_path)

        if not blobs:
            logger.warning(f"No blobs found in {bucket_name}/{source_folder_path}")
            return

        for blob in blobs:
            if blob.name.endswith("/"):
                continue  # Skip "folders"
            dest_file_path = os.path.join(
                local_dest_path, os.path.relpath(blob.name, source_folder_path)
            )
            os.makedirs(os.path.dirname(dest_file_path), exist_ok=True)
            blob.download_to_filename(dest_file_path)
            logger.info(f"Downloaded {blob.name} to {dest_file_path}")
    except GoogleCloudError as e:
        logger.error(
            f"Failed to download files from {bucket_name}/{source_folder_path}: {e}"
        )
        raise RuntimeError(
            f"Failed to download files from {bucket_name}/{source_folder_path}"
        ) from e
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        raise