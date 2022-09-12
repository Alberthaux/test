import glob


def get_gallery(page):
    dir_list = glob.glob(f'app/static/photos/{page}/*')
    dir_list = [
        f'../static/photos/{page}/' + d.split('/')[-1]
        for d in dir_list
    ]
    dir_list.sort()
    return dir_list
