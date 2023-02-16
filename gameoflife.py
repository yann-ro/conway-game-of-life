import pygame
import numpy as np


class GameofLife:
    def __init__(
        self,
        surface,
        init_type=None,
        width=1920,
        height=1080,
        scale=10,
        offset=1,
        active_color=(255, 255, 255),
        inactive_color=(50, 50, 50),
    ):
        """_summary_

        Args:
            surface (_type_): _description_
            init_type (_type_, optional): _description_. Defaults to None.
            width (int, optional): _description_. Defaults to 1920.
            height (int, optional): _description_. Defaults to 1080.
            scale (int, optional): _description_. Defaults to 10.
            offset (int, optional): _description_. Defaults to 1.
            active_color (tuple, optional): _description_. Defaults to (255, 255, 255).
            inactive_color (tuple, optional): _description_. Defaults to (50, 50, 50).
        """
        self.surface = surface
        self.width = width
        self.height = height
        self.scale = scale
        self.offset = offset
        self.active_color = active_color
        self.inactive_color = inactive_color

        self.columns = int(height / scale)
        self.rows = int(width / scale)

        self.init_pos = [10, 10]

        if init_type:
            self.grid = np.zeros((self.rows, self.columns), dtype=bool)
            with open(f"item/{init_type}.npy", "rb") as f:
                self.add_to_init(np.load(f).T)
        else:
            self.grid = np.random.randint(
                0, 2, size=(self.rows, self.columns), dtype=bool
            )

    def add_to_init(self, item):
        """_summary_

        Args:
            item (_type_): _description_
        """
        self.grid[
            self.init_pos[0] : self.init_pos[0] + item.shape[0],
            self.init_pos[1] : self.init_pos[1] + item.shape[1],
        ] = item

    def run(self):
        """Update and redraw the current grid state
        """
        self.draw_grid()
        self.update_grid()

    def draw_grid(self):
        """
        Drawing the grid
        """
        for row in range(self.rows):
            for col in range(self.columns):
                if self.grid[row, col]:
                    pygame.draw.rect(
                        self.surface,
                        self.active_color,
                        [
                            row * self.scale,
                            col * self.scale,
                            self.scale - self.offset,
                            self.scale - self.offset,
                        ],
                    )
                else:
                    pygame.draw.rect(
                        self.surface,
                        self.inactive_color,
                        [
                            row * self.scale,
                            col * self.scale,
                            self.scale - self.offset,
                            self.scale - self.offset,
                        ],
                    )

    def update_grid(self):
        """
        Updating the grid based on Conway's game of life rules
        """
        updated_grid = self.grid.copy()
        for row in range(updated_grid.shape[0]):
            for col in range(updated_grid.shape[1]):
                updated_grid[row, col] = self.update_cell(row, col)

        self.grid = updated_grid

    def update_cell(self, x, y):
        """
        Update single cell based on Conway's game of life rules.
        /!\ bug on borders : need to be fixed
        """
        current_state = self.grid[x, y]
        alive_neighbors = 0

        # Get to how many alive neighbors
        for i in range(-1, 2):
            for j in range(-1, 2):
                try:
                    if i == 0 and j == 0:
                        continue
                    elif self.grid[x + i, y + j]:
                        alive_neighbors += 1
                except:
                    continue

        # Updating the cell's state
        if current_state and alive_neighbors < 2:  # dies: underpopulation
            return False
        elif current_state and alive_neighbors > 3:  # dies: overpopulation
            return False
        elif current_state and (
            alive_neighbors == 2 or alive_neighbors == 3
        ):  # stay alive
            return True
        elif ~current_state and alive_neighbors == 3:  # born: reproduction
            return True
        else:
            return current_state
