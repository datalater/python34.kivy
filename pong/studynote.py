#:kivy 1.9.1

<PongGame>:
    canvas:
        Rectangle:
			pos: self.center_x - 5, 0
			size: 10, self.height
		Rectangle:
			pos: 0, self.center_y - 5
			size: self.width, 10
    Label:
        font_size: 70
        center_x: root.width / 4
        top: root.top - 50
        text: "0"

    Label:
        font_size: 70
        center_x: root.width * 3 / 4
        top: root.top - 50
        text: "0"
