"""A video player class."""
from dbm.ndbm import library

from .video_library import VideoLibrary


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        print("Here's a list of all available videos: \n")
        library = VideoLibrary()
        for video in library.get_all_videos():
            print(f"{video.title} ({video.video_id}) {list(video.tags)} \n")

        print("show_all_videos needs implementation")

    def play_video(self, video_id):
        """Plays the respective video."""
        print("The video that is being played: \n")
        library = VideoLibrary()
        """Args:
            video_id: The video_id to be played."""
        for video in library.play_video(): print (f"{video.title} ({video.video_id}) {list(video.tags)} \n")
        print("play_video needs implementation")

    def stop_video(self):
        """Stops the current video."""
        print ("The video that is being stopped: \n")
        library = VideoLibrary()
        for video in library.stop_video():
            print (f"{video.title} ({video.video_id}) {list(video.tags)} \n")
        print("stop_video needs implementation")

    def play_random_video(self):
        """Plays a random video from the video library."""
        print("A random video that is being played: \n")
        library = VideoLibrary()
        for video in library.play_random_video():
            print (f"{video.title} ({video.video_id}) {list(video.tags)} \n")
        print("play_random_video needs implementation")

    def pause_video(self):
        """Pauses the current video."""
        print("A video that is being paused: \n")
        library = VideoLibrary()
        for video in library.pause_video():
            print (f"{video.title} ({video.video_id}) {list(video.tags)} \n")
        print("pause_video needs implementation")

    def continue_video(self):
        """Resumes playing the current video."""
        print(" A video that is currently being paused and is being resumed: \n")
        library = VideoLibrary()
        for video in library.continue_video():
            print(f"{video.title} ({video.video_id}) {list(video.tags)} \n")
        print("continue_video needs implementation")

    def show_playing(self):
        """Displays video currently playing."""
        print("A video that is currently being played: \n")
        library = VideoLibrary()
        for video in library.show_playing():
            print (f"{video.title} ({video.video_id}) {list(video.tags)} \n")
        print("show_playing needs implementation")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name."""
        print("A playlist that is currently being created: \n")
        """Args:
            playlist_name: The playlist name."""
        for video in library.create_playlist():
            print(f"{video.title} ({video.video_id}) {list(video.tags)} \n")
        print("create_playlist needs implementation")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name."""
        print("A playlist that is being added to: \n")
        """Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added."""
        for video in library.add_to_playlist():
            print (f"{video.title} ({video.video_id}) {list(video.tags)} \n")
        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""
        print("A playlist that is being shown: \n")
        for video in library.show_all_playlists():
            print(f"{video.title} ({video.video_id}) {list(video.tags)} \n")
        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name."""
        print("A playlist that is being shown: \n")
        for video in library.show_playlist
         """Args:
            playlist_name: The playlist name."""
        for video in library.show_playlist():
            print(f"{video.title} ({video.video_id}) {list(video.tags)}")
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name."""
        print("A video that is being removed from the playlist: \n")

        """Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed."""
        for video in library.remove_from_playlist():
            print(f"{video.title} ({video.video_id}) {list(video.tags)}")
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name."""
        print("All videos are being removed from the playlist: \n")

        """Args:
            playlist_name: The playlist name."""
        for video in library.clear_playlist():
            print(f"{video.title} ({video.video_id}) {list(video.tags)}")
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name."""
        print("A playlist that is being deleted: \n")
        """Args:
            playlist_name: The playlist name."""
        for video in library.delete_playlist():
            print(f"{video.title} ({video.video_id}) {list(video.tags)}")
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term."""
        print("Videos that are being shown according to a specific search term: \n")


        """Args:
            search_term: The query to be used in search."""
        for video in library.search_videos():
            print(f"{video.title} ({video.video_id}) {list(video.tags)}")
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag."""
        print("Videos that are being shown that contains the provided video tag: \n")

        """Args:
            video_tag: The video tag to be used in search."""
        for video in library.search_videos_tag():
            print(f"{video.title} ({video.video_id}) {list(video.tags)}")
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged."""
        print("Videos that are being currently flaggged: \n")

        """Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video."""
        for video in library.search_videos_tag():
            print(f"{video.title} ({video.video_id}) {list(video.tags)}")
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video."""
        print("Videos that are having a flag being removed: \n")
        """Args:
            video_id: The video_id to be allowed again."""
        for video in library.allow_video():
            print(f"{video.title} ({video.video_id}) {list(video.tags)}")
        print("allow_video needs implementation")
