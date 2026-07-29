import visual.managers.manager as manager
import config

class CharacterManager(manager.Manager):
    def test(self):
        for n, i in enumerate(self.buttons):
            print(n, i.name)
        for n, i in enumerate(self.id_objects):
            print(n, i)

    def active(self):
        self.test()
        for i in range(2, 2 + config.quantity_frames):
            if self.buttons[i].on:
                id_object = self.id_objects[3 * (i - 2) + 2]
                self.display.show(id_object)
            else:
                id_object = self.id_objects[3 * (i - 2) + 2]
                self.display.hide(id_object)

