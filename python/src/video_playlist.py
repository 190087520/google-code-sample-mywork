"""A video playlist class."""

from .video_library import VideoLibrary


def __init__(self):
    self._video_library = VideoLibrary()
class Playlist:
    """A class used to represent a Playlist."""


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
