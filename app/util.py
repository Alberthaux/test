import glob


def get_gallery(page):
    dir_list = glob.glob(f'static/photos/{page}/*')
    dir_list = [
        f'../static/photos/{page}/' + d.split('/')[-1]
        for d in dir_list
    ]
    return dir_list
