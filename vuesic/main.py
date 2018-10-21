import zipfile
import os

from PIL import Image
import click

@click.group()
def main():
  pass


@click.command()
@click.argument('path')
@click.argument('region')
def crop(path, region):
  """Crop an set of images. Use 444,576,1920,1054 for panels and 0,0,442,1058 for the side drawer."""
  directory = os.path.dirname(path)
  zip = zipfile.ZipFile(path, 'r')
  images = zip.namelist()
  click.echo(f'Found {len(images)} images in {path}')
  zip.extractall(directory)
  zip.close()

  for file in images:
    name, ext = file.split('.')
    src = os.path.join(directory, file) 
    dst = os.path.join(directory, f'{name}-cropped.{ext}')

    img = Image.open(src)
    area = list(map(int, region.split(',')))
    if len(area) != 4:
      click.echo('4 values must be provided for the `region`')
      raise click.Abort

    cropped_img = img.crop(area)

    click.echo(f'Saving image to {dst}')
    cropped_img.save(dst)


main.add_command(crop)

if __name__ == '__main__':
  main()
