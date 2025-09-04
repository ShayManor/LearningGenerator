import boto3
from typing import BinaryIO

from src.app.gateways.storage.storage import Storage


class S3Storage(Storage):
    def __init__(self, bucket: str, region: str = "us-east-1"):
        self.bucket = bucket
        self.s3 = boto3.client("s3", region_name=region)

    def upload(self, file: BinaryIO, key: str, content_type: str) -> str:
        self.s3.upload_fileobj(
            file, self.bucket, key, ExtraArgs={"ContentType": content_type}
        )
        return f"https://{self.bucket}.s3.amazonaws.com/{key}"

    def delete(self, key: str) -> None:
        self.s3.delete_object(Bucket=self.bucket, Key=key)
