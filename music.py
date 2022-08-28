from msilib.schema import Class
import winsound


class Music():
    def play_Background_music(self):
        winsound.PlaySound("Background_Music.wav",winsound.SND_ASYNC)

    def play_Wall_Collision(self):
        winsound.PlaySound("Wall_Collision.wav",winsound.SND_ASYNC)

    def play_Paddle_Collision(self):
        winsound.PlaySound("paddle_hit.wav",winsound.SND_ASYNC)

    def play_Winning_Sound(self):
        winsound.PlaySound("Last_Winning_Sound.wav",winsound.SND_ASYNC) 