"""This handles files and streaming use-cases"""
import ffmpeg_streaming
from ffmpeg_streaming import S3
from ffmpeg_streaming import GCS
from ffmpeg_streaming import MAS
from ffmpeg_streaming import CloudManager
from ffmpeg_streaming._input import Input


class Connect(object):
    '''This class handles files and streaming use cases
    Will do with any cloud infrastructure'''

    # Cloud type: Amazon_S3, Google_Cloud, Microsoft_Azure
    def __init__(self, cloud_type: str) -> None:
        self.cloud_type = cloud_type

    # get cloud instance:
    def connect_with_amazon_cloud(self,
                                  aws_access_key_id: str,
                                  aws_secret_access_key: str,
                                  region_name: str,
                                  bucket_name: str,
                                  asset_name: str
                                  ) -> Input:

        if self.cloud_type == "Amazon_S3":
            amazon_cloud = S3(aws_access_key_id=aws_access_key_id,
                              aws_secret_access_key=aws_secret_access_key,
                              region_name=region_name
                              )
            cloud_file: Input = ffmpeg_streaming.input(amazon_cloud, bucket_name=bucket_name, key=asset_name)
            return cloud_file

    def connect_with_google_cloud(self):
        if self.cloud_type == "Google_Cloud":
            # you might want to find out this when there is internet:
            pass
        pass

    def connect_with_microsoft_cloud(self):
        if self.cloud_type == "Microsoft_Azure":
            # you might want to find out this when there is internet:
            pass
        pass
