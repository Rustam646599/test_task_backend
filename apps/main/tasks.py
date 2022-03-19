from core.libs.celery import app
from core.libs.utils import download_video
from loguru import logger
from apps.main.models.posts import VideoPost


@app.task(ignore_result=True)
def post_video_download(video_post_id: int):
    """Скачивает полученное видео"""

    try:
        video_post = VideoPost.objects.get(id=video_post_id)
        video_post.video.save(video_post.video_url.split('/')[-1], download_video(video_post.video_url))
        video_post.is_download = True
        video_post.save()
    except VideoPost.DoesNotExist:
        logger.info('Пост не найден')
    except Exception as e:
        logger.info(str(e))
