"""A video player class."""

from .video_library import VideoLibrary
import random

class VideoPlayer:
    """A class used to represent a Video Player."""
    video_playing = False #Stop Playing
    video_paused = False
    video_stopped = False
    previous_video_title = ""

    playlist_created = ""
    playlist_created_flag = False
    added_video_title = ""
    video_in_playlist = []
    video_added_flag = False
    all_playlists_created = []

    def __init__(self):
        self._video_library = VideoLibrary()

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        print("Here's a list of all available videos: ")
        all_videos = self._video_library.get_all_videos()
        n = 0
        video_sorting = []

        for n in range(len(all_videos)):
            video_sorting.append(all_videos[n].video_id)
        video_sorting.sort()
        for n in range(len(all_videos)):
            sorted_video_title = self._video_library.get_video(video_sorting[n])
            video_tags = [i.strip("''") for i in (sorted_video_title.tags)]
            print(f"{sorted_video_title.title} ({sorted_video_title.video_id}) {'[%s]'%' ' .join(map(str,video_tags))}")

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        #print("play_video needs implementation")
        if self._video_library.get_video(video_id) != None:
            if self.video_playing == False and self.video_paused == False:
                self.previous_video_title = self._video_library.get_video(video_id)
                print(f"Playing video: {self.previous_video_title.title}")
                self.video_playing = True
            else:
                print(f"Stopping video: {self.previous_video_title.title}")
                self.current_video_title = self._video_library.get_video(video_id)
                print(f"Playing video: {self.current_video_title.title}")
                self.video_playing = True
                self.video_paused = False
                self.previous_video_title = self.current_video_title
        else:
            print(f"Cannot play video: Video does not exist")
            self.video_playing = False

    def stop_video(self):
        """Stops the current video."""

        #print("stop_video needs implementation")
        if self.video_playing == True and (self.video_paused == False):
            self.current_video_title = self.previous_video_title.title
            print(f"Stopping video: {self.previous_video_title.title}")
            self.video_playing = False
            self.video_paused = False
            self.video_stopped = True
        elif self.video_playing == False and (self.video_paused == True):
            print(f"Stopping video: {self.previous_video_title.title}")
            self.video_stopped = True
            self.video_playing = False
            self.video_paused = False
        else:
            print("Cannot stop video: No video is currently playing")

    def play_random_video(self):
        """Plays a random video from the video library."""

        #print("play_random_video needs implementation")
        #Generate random number
        ran_num = random.randint(1, len(self._video_library.get_all_videos()))
        videos_available = self._video_library.get_all_videos()
        self.play_video(videos_available[ran_num-1].video_id)
       
    def pause_video(self):
        """Pauses the current video."""

        #print("pause_video needs implementation")
        if (self.video_playing == True) and (self.video_paused == False):
            print(f"Pausing video: {self.previous_video_title.title}")
            self.video_paused = True
            self.video_playing = False
        elif (self.video_paused == True) and (self.video_playing == False):
            print(f"Video already paused: {self.previous_video_title.title}")
        else:
            print("Cannot pause video: No video is currently playing")

    def continue_video(self):
        """Resumes playing the current video."""

        #print("continue_video needs implementation")
        if self.video_playing == False and (self.video_paused == True):
            print(f"Continuing video: {self.previous_video_title.title}")
            self.video_paused = False
            self.video_playing = True
        elif self.video_playing == True and (self.video_paused == False):
            print("Cannot continue video: Video is not paused")
        else:
            print("Cannot continue video: No video is currently playing")


    def show_playing(self):
        """Displays video currently playing."""

        #print("show_playing needs implementation")

        if self.video_playing == True and (self.video_paused == False):
            video_tags = [i.strip("''") for i in (self.previous_video_title.tags)]
            print(f"Currently playing: {self.previous_video_title.title} ({self.previous_video_title.video_id}) {'[%s]'%' ' .join(map(str,video_tags))}")
        elif self.video_paused == True and (self.video_playing == False) and (self.video_stopped == False):
            video_tags = [i.strip("''") for i in (self.previous_video_title.tags)]
            print(f"Currently playing: {self.previous_video_title.title} ({self.previous_video_title.video_id}) {'[%s]'%' ' .join(map(str,video_tags))} - PAUSED")
        else:
            print("No video is currently playing")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        #print("create_playlist needs implementation")
        self.playlist_created = playlist_name.lower()
        if self.playlist_created_flag == False:
            print(f"Successfully created new playlist: {playlist_name}")
            self.all_playlists_created.append(playlist_name)
            self.playlist_created_flag = True
        else:
            print("Cannot create playlist: A playlist with the same name already exists")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        #print("add_to_playlist needs implementation")
        self.added_video_title = self._video_library.get_video(video_id)
        #self.video_in_playlist.append(self.added_video_title.title)
        
        if playlist_name.lower() == self.playlist_created:
            if self.added_video_title != None and self.added_video_title.title not in self.video_in_playlist:
                self.video_in_playlist.append(self.added_video_title.title)
                video_name = [i.strip("''") for i in (self.video_in_playlist)]
                print(f"Added video to {playlist_name}: {'%s'%' ' .join(map(str,video_name))}")
            elif (self.added_video_title == None):
                print(f"Cannot add video to {playlist_name}: Video does not exist")
            elif self.added_video_title.title in self.video_in_playlist:
                print(f"Cannot add video to {playlist_name}: Video already added")
        elif playlist_name.lower() != self.playlist_created:
            if self.added_video_title == None:
                print(f"Cannot add video to {playlist_name}: Playlist does not exist")
            elif self.added_video_title.title in self.video_in_playlist:
                print(f"Cannot add video to {playlist_name}: Playlist does not exist")

    def show_all_playlists(self):
        """Display all playlists."""

        #print("show_all_playlists needs implementation")
        if len(self.all_playlists_created) == 0:
            print("No playlists exist yet")
        else:
            for i in range(len(self.all_playlists_created)):
                print("Showing all playlists:")
                for j in self.all_playlists_created:
                    print(j)


    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        #print("show_playlist needs implementation")
        if len(self.video_in_playlist) == 0:
            print(f"Showing playlist: {playlist_name}")
            print("  No videos here yet.")
        elif playlist_name.lower() != self.playlist_created:
            print(f"Cannot show playlist {playlist_name}: Playlist does not exist")
        else:
            print(f"Showing playlist: {playlist_name}")
            video_name = [i.strip("''") for i in (self.added_video_title)]
            print(f"  {self.added_video_title.title} ({self.added_video_title.video_id}) {'[%s]'%' ' .join(map(str,video_name))}")


    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        #print("remove_from_playlist needs implementation")
        self.remove_video = self._video_library.get_video(video_id)

        if self.remove_video != None:
            if  playlist_name.lower() == self.playlist_created:
                if self.remove_video.title in self.video_in_playlist:
                    self.video_in_playlist.remove(self.remove_video.title)
                    print(f"Removed video from {playlist_name}: {self.remove_video.title}")
                elif self.remove_video.title not in self.video_in_playlist:
                    print(f"Cannot remove video from {playlist_name}: Video is not in playlist")
            else:
                print(f"Cannot remove video from {playlist_name}: Playlist does not exist")
        elif self.remove_video == None:
            if playlist_name.lower() == self.playlist_created:
                print(f"Cannot remove video from {playlist_name}: Video does not exist")
            else:
                print(f"Cannot remove video from {playlist_name}: Playlist does not exist")
        

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        #print("clears_playlist needs implementation")
        if playlist_name.lower() == self.playlist_created:
            for i in range(len(self.video_in_playlist)):
                if i >= 0 :
                    self.video_in_playlist.clear()
                    print(f"Successfully removed all videos from {playlist_name}")
        elif playlist_name.lower() != self.playlist_created:
            print(f"Cannot clear playlist {playlist_name}: Playlist does not exist")
        else:
            print("Error")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        #print("deletes_playlist needs implementation")
        if self.playlist_created != 0:
            if playlist_name in self.all_playlists_created:
                print(f"Deleted playlist: {playlist_name}")
                self.all_playlists_created.remove(playlist_name)
            else:
                print(f"Cannot delete playlist {playlist_name}: Playlist does not exist")


    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        #print("search_videos needs implementation")
        

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def video_playing_video(self, video_id, video_playing_reason=""):
        """Mark a video as video_playingged.

        Args:
            video_id: The video_id to be video_playingged.
            video_playing_reason: Reason for video_playingging the video.
        """
        print("video_playing_video needs implementation")

    def allow_video(self, video_id):
        """Removes a video_playing from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
