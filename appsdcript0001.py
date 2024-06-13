# このスクリプトは、YouTubeの文字お越しをPythonで作成し、作成した文字を校正処理します。

import youtube_dl
import re
from dataclasses import dataclass

@dataclass
class YouTubeVideo:
    """YouTube動画の情報を保持するクラス"""
    title: str
    description: str

def download_youtube_video(video_url: str) -> YouTubeVideo:
    """YouTube動画をダウンロードし、動画の情報を返す"""
    ydl_opts = {'outtmpl': '%(id)s.%(ext)s'}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(video_url, download=True)
        title = info_dict.get('title', '')
        description = info_dict.get('description', '')
        return YouTubeVideo(title, description)

def correct_text(text: str) -> str:
    """文字を校正処理"""
    # ここでは簡単な文字の校正処理を行う
    text = re.sub(r'[^\w\s]', '', text)  # 非アルファベット文字を削除
    return text

def main():
    video_url = input("YouTube動画のURLを入力してください：")
    video = download_youtube_video(video_url)
    print("動画タイトル：", video.title)
    print("動画説明：", video.description)
    corrected_text = correct_text(video.description)
    print("校正された説明：", corrected_text)

if __name__ == "__main__":
    main()