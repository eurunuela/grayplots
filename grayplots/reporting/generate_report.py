import os


def generate_report(images_html, outdir):
    html_filename = 'grayplots.html'
    if os.path.isfile(os.path.join(outdir, html_filename)):
        os.remove(os.path.join(outdir, html_filename))
    f = open(os.path.join(outdir, html_filename), 'w')

    html_code = """<html>
    <head></head>
    <body><center>
    {0}
    </center></body>
    </html>""".format(images_html)

    f.write(html_code)
    f.close()


def generate_image(image_path, dim, title):
    image_title = f'<h2>{title}</h2>'
    image_html = f'<img src="{image_path}" width="{dim[0]}" height="{dim[1]}">'
    return image_title + image_html
