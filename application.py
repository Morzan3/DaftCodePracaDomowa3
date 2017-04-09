import os
from flask import Flask, render_template, request, redirect, abort
from walker_wrapper import *
import urllib
app = Flask(__name__)

@app.route('/stats', methods=['GET'])
def redirect():
    return redirect("/stats/test%20dir", code=302)

@app.route("/stats/<path:my_path>", methods=['GET'])
def return_stats(my_path):
    my_path = urllib.parse.unquote_plus(urllib.parse.unquote_plus(my_path))
    if not check_if_exists(my_path):
        return render_template('404.html'), 404
    folder_size = get_main_folder_size(my_path)
    parent = get_parent(my_path)
    children_files, children_folders = get_children(my_path)
    return render_template('folder_stats.html', children_files=children_files, children_folders=children_folders, folder_name=my_path, folder_size = folder_size , parent_name = parent, parent_path = urllib.parse.quote_plus(parent))

if __name__ == "__main__":
    app.run()
