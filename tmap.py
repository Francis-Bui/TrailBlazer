class Map:
    def __init__(self, img, max_height_diff, dist_between_pixels):
        self.img = img
        self.height = img.shape[0]
        self.width = img.shape[1] 
        self.max_height_diff = max_height_diff
        self.dist_between_pixels = dist_between_pixels
        self.height_map = self.generate_height_map()

    def calculate_height(self, r, g, b):
        normalized = ((r * 255 * 255) + (g * 255) + (b)) / \
            (255**3 + 255**2 + 255)
        return normalized * self.max_height_diff
        # placeholder for height calculator

    def generate_height_map(self):
        img_height = self.img.shape[0]
        img_width = self.img.shape[1]

        height_map = [x[:] for x in [[0] * img_width] * img_height]
        for i in range(0, img_height):
            for j in range(0, img_width):
                # Calculate height based on rgb values
                height_map[i][j] = self.calculate_height(
                    self.img[i, j, 0],
                    self.img[i, j, 1],
                    self.img[i, j, 2]
                )
        return height_map
