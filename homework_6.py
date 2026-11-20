class Streamer:
    def live(self):
        return "Запускаю стрим! Подписывайтесь, ставьте лайки!"

    def earn(self):
        return "Заработал 500 донатов за 2 часа"


class TikToker:
    def live(self):
        return "Снимаю трендовый тикток под песню месяца!"

    def viral(self):
        return "Набрал 3 миллиона просмотров за сутки!"


class Mutant:
    def live(self):
        return "Я... я свечусь в темноте... это мой вайб..."

    def superpower(self):
        return "Летаю и стреляю лазерами из глаз"


# Streamer стоит первым, поэтому live() берётся у Streamer.
# Если поменять родителей местами, live() будет вызываться у Mutant.
class GlowStreamer(Streamer, Mutant):
    def ultimate_content(self):
        return f"{self.live()} {self.superpower()} {self.earn()}"


# TikToker стоит первым, поэтому live() берётся у TikToker.
# Если поменять родителей местами, live() будет вызываться у Mutant.
class ViralCyborg(TikToker, Mutant):
    def ultimate_content(self):
        return f"{self.live()} {self.superpower()} {self.viral()}"


# Streamer стоит первым, поэтому live() берётся у Streamer.
# Если поменять родителей местами, live() будет вызываться у TikToker.
class DonateMage(Streamer, TikToker):
    def ultimate_content(self):
        return f"{self.live()} {self.viral()} {self.earn()}"


def show_character(character):
    print(f"\n{character.__class__.__name__}")
    print("MRO:", [cls.__name__ for cls in character.__class__.mro()])
    print("live():", character.live())
    print("ultimate_content():", character.ultimate_content())


glow = GlowStreamer()
cyborg = ViralCyborg()
mage = DonateMage()

show_character(glow)
show_character(cyborg)
show_character(mage)
