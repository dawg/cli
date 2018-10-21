import zipfile
import enum
import os

from PIL import Image
import click

SIDEBAR = (0, 0, 442, 1058)
LOWERBAR = (444, 576, 1920, 1054)

@click.group()
def main():
  pass


@click.command()
@click.argument('src')
@click.argument('dst')
def sidebar(src, dst):
  """Crop an set of images."""
  join(src, dst, SIDEBAR, Direction.HORIZONTAL)

@click.command()
@click.argument('src')
@click.argument('dst')
def lowerbar(src, dst):
  """Crop an set of images."""
  join(src, dst, LOWERBAR, Direction.VERTICAL)

class Direction(enum.Enum):
  HORIZONTAL = 1
  VERTICAL = 2

def join(src: str, dst: str, area: tuple, direction: Direction):
  directory = os.path.dirname(src)
  zip_file = zipfile.ZipFile(src, 'r')
  files = zip_file.namelist()
  click.echo(f'Found {len(files)} images in {src}')
  zip_file.extractall(directory)
  zip_file.close()

  def make_path(file):
    return os.path.join(directory, file)

  def crop(image):
    return image.crop(area)

  def show(image):
    # image.show()
    return image

  paths = map(make_path, files)
  images = map(Image.open, paths)
  images = map(crop, images)
  images = list(map(show, images))
  
  widths, heights = zip(*(i.size for i in images))
  print(widths, heights)

  if direction == Direction.HORIZONTAL:
    width = sum(widths)
    height = max(heights)
  else:
    width = max(widths)
    height = sum(heights)
  
  click.echo(f'Creating image {width} x {height}')
  new_im = Image.new('RGB', (width, height))

  box = [0, 0]
  for im in images:
    new_im.paste(im, tuple(box))

    if direction == Direction.HORIZONTAL:
      box[0] += im.size[0]
    else:
      box[1] += im.size[1]

  click.echo(f'Saving image to {os.path.abspath(dst)}')
  new_im.save(dst)


main.add_command(sidebar)
main.add_command(lowerbar)

if __name__ == '__main__':
  main()
