# Module: main
# Author: Roman V. M.
# Created on: 28.11.2014
# License: GPL v.3 https://www.gnu.org/copyleft/gpl.html
"""
Example video plugin that is compatible with Kodi 19.x "Matrix" and above
"""
import sys
from urllib.parse import urlencode, parse_qsl
import xbmcgui
import xbmcplugin

# Get the plugin url in plugin:// notation.
_URL = sys.argv[0]
# Get the plugin handle as an integer number.
_HANDLE = int(sys.argv[1])

# Free sample videos are provided by www.vidsplay.com
# Here we use a fixed set of properties simply for demonstrating purposes
# In a "real life" plugin you will need to get info and links to video files/streams
# from some web-site or online service.
VIDEOS = {'Private Sex Tapes': [{'name': 'Daniela Paralis: Beine breit du Schlampe',
                       'thumb': 'http://worldofwarcry.sytes.net:8091/dworlds/media/pictures/vlcsnap-2022-04-14-12h05m55s262.png',
                       'video': 'http://worldofwarcry.sytes.net:8091/dworlds/media/daniela/20140508_084451.mp4',
                       'genre': 'Amateure'},
                      {'name': 'Daniela Paralis: In der Periode gefickt',
                       'thumb': 'http://worldofwarcry.sytes.net:8091/dworlds/media/pictures/vlcsnap-2022-04-14-12h06m53s028.png',
                       'video': 'http://worldofwarcry.sytes.net:8091/dworlds/media/daniela/20140627_162346.mp4',
                       'genre': 'Amateure'},
                      {'name': 'Daniela Paralis: Traumhaft schöne Muschi',
                       'thumb': 'http://worldofwarcry.sytes.net:8091/dworlds/media/pictures/vlcsnap-2022-04-14-12h07m11s684.png',
                       'video': 'http://worldofwarcry.sytes.net:8091/dworlds/media/daniela/20140508_084799.mp4',
                       'genre': 'Amateure'}
                      ],
            'Chaturbate Records': [{'name': '111542',
                      'thumb': 'http://worldofwarcry.sytes.net:8091/dworlds/media/pictures/001.png',
                      'video': 'http://worldofwarcry.sytes.net:8091/dworlds/media/chats/111542.mp4',
                      'genre': 'Cars'},
                     {'name': '20220413_035610',
                      'thumb': 'http://worldofwarcry.sytes.net:8091/dworlds/media/pictures/002.png',
                      'video': 'http://worldofwarcry.sytes.net:8091/dworlds/media/chats/20220413_035610.mp4',
                      'genre': 'Cars'},
		     {'name': '20220413_045341',
                      'thumb': 'http://worldofwarcry.sytes.net:8091/dworlds/media/pictures/003.png',
                      'video': 'http://worldofwarcry.sytes.net:8091/dworlds/media/chats/20220413_045341.mp4',
                      'genre': 'Cars'},
		     {'name': '20220413_234135',
                      'thumb': 'http://worldofwarcry.sytes.net:8091/dworlds/media/pictures/004.png',
                      'video': 'http://worldofwarcry.sytes.net:8091/dworlds/media/chats/20220413_234135.mp4',
                      'genre': 'Cars'},
		     {'name': 'Traffic',
                      'thumb': 'http://worldofwarcry.sytes.net:8091/dworlds/media/pictures/005.png',
                      'video': 'http://worldofwarcry.sytes.net:8091/dworlds/media/chats/20220414_020304.mp4',
                      'genre': 'Cars'},
		     {'name': 'Traffic',
                      'thumb': 'http://worldofwarcry.sytes.net:8091/dworlds/media/pictures/006.png',
                      'video': 'http://worldofwarcry.sytes.net:8091/dworlds/media/chats/20220414_035758.mp4',
                      'genre': 'Cars'},
		     {'name': 'Traffic',
                      'thumb': 'http://worldofwarcry.sytes.net:8091/dworlds/media/pictures/007.png',
                      'video': 'http://worldofwarcry.sytes.net:8091/dworlds/media/chats/20220414_041100.mp4',
                      'genre': 'Cars'},
		     {'name': 'Traffic',
                      'thumb': 'http://worldofwarcry.sytes.net:8091/dworlds/media/pictures/008.png',
                      'video': 'http://worldofwarcry.sytes.net:8091/dworlds/media/chats/20220414_071311.mp4',
                      'genre': 'Cars'},
                     {'name': 'Traffic Arrows',
                      'thumb': 'http://worldofwarcry.sytes.net:8091/dworlds/media/pictures/009.png',
                      'video': 'http://worldofwarcry.sytes.net:8091/dworlds/media/chats/20220414_071321_edit1.mp4',
                      'genre': 'Cars'}
                     ],
            'Mia Milagros': [{'name': 'August 17 2021 02 54 11',
                      'thumb': 'http://worldofwarcry.sytes.net:8091/dworlds/media/pictures/vlcsnap-2022-04-15-11h09m46s760.png',
                      'video': 'http://worldofwarcry.sytes.net:8091/dworlds/media/chats/Mia%20Milagros/August%2017%202021%2002%2054%2011.mp4',
                      'genre': 'Perfect Teen'},
                     {'name': 'August 17 2021 03 22 28',
                      'thumb': 'http://worldofwarcry.sytes.net:8091/dworlds/media/pictures/vlcsnap-2022-04-15-11h09m55s736.png',
                      'video': 'http://worldofwarcry.sytes.net:8091/dworlds/media/chats/Mia%20Milagros/August%2017%202021%2003%2022%2028.mp4',
                      'genre': 'Perfect Teen'},
                     {'name': 'Blue Eyed Dream with Perfect Tits',
                      'thumb': 'http://worldofwarcry.sytes.net:8091/dworlds/media/pictures/vlcsnap-2022-04-15-11h10m27s162.png',
                      'video': 'http://worldofwarcry.sytes.net:8091/dworlds/media/chats/Mia%20Milagros/Blue%20Eyed%20Dream%20with%20Perfect%20Tits.mp4',
                      'genre': 'Perfect Teen'}
                     ]}


def get_url(**kwargs):
    """
    Create a URL for calling the plugin recursively from the given set of keyword arguments.

    :param kwargs: "argument=value" pairs
    :return: plugin call URL
    :rtype: str
    """
    return '{}?{}'.format(_URL, urlencode(kwargs))


def get_categories():
    """
    Get the list of video categories.

    Here you can insert some parsing code that retrieves
    the list of video categories (e.g. 'Movies', 'TV-shows', 'Documentaries' etc.)
    from some site or API.

    .. note:: Consider using `generator functions <https://wiki.python.org/moin/Generators>`_
        instead of returning lists.

    :return: The list of video categories
    :rtype: types.GeneratorType
    """
    return VIDEOS.keys()


def get_videos(category):
    """
    Get the list of videofiles/streams.

    Here you can insert some parsing code that retrieves
    the list of video streams in the given category from some site or API.

    .. note:: Consider using `generators functions <https://wiki.python.org/moin/Generators>`_
        instead of returning lists.

    :param category: Category name
    :type category: str
    :return: the list of videos in the category
    :rtype: list
    """
    return VIDEOS[category]


def list_categories():
    """
    Create the list of video categories in the Kodi interface.
    """
    # Set plugin category. It is displayed in some skins as the name
    # of the current section.
    xbmcplugin.setPluginCategory(_HANDLE, 'My Video Collection')
    # Set plugin content. It allows Kodi to select appropriate views
    # for this type of content.
    xbmcplugin.setContent(_HANDLE, 'videos')
    # Get video categories
    categories = get_categories()
    # Iterate through categories
    for category in categories:
        # Create a list item with a text label and a thumbnail image.
        list_item = xbmcgui.ListItem(label=category)
        # Set graphics (thumbnail, fanart, banner, poster, landscape etc.) for the list item.
        # Here we use the same image for all items for simplicity's sake.
        # In a real-life plugin you need to set each image accordingly.
        list_item.setArt({'thumb': VIDEOS[category][0]['thumb'],
                          'icon': VIDEOS[category][0]['thumb'],
                          'fanart': VIDEOS[category][0]['thumb']})
        # Set additional info for the list item.
        # Here we use a category name for both properties for for simplicity's sake.
        # setInfo allows to set various information for an item.
        # For available properties see the following link:
        # https://codedocs.xyz/xbmc/xbmc/group__python__xbmcgui__listitem.html#ga0b71166869bda87ad744942888fb5f14
        # 'mediatype' is needed for a skin to display info for this ListItem correctly.
        list_item.setInfo('video', {'title': category,
                                    'genre': category,
                                    'mediatype': 'video'})
        # Create a URL for a plugin recursive call.
        # Example: plugin://plugin.video.example/?action=listing&category=Animals
        url = get_url(action='listing', category=category)
        # is_folder = True means that this item opens a sub-list of lower level items.
        is_folder = True
        # Add our item to the Kodi virtual folder listing.
        xbmcplugin.addDirectoryItem(_HANDLE, url, list_item, is_folder)
    # Add a sort method for the virtual folder items (alphabetically, ignore articles)
    xbmcplugin.addSortMethod(_HANDLE, xbmcplugin.SORT_METHOD_LABEL_IGNORE_THE)
    # Finish creating a virtual folder.
    xbmcplugin.endOfDirectory(_HANDLE)


def list_videos(category):
    """
    Create the list of playable videos in the Kodi interface.

    :param category: Category name
    :type category: str
    """
    # Set plugin category. It is displayed in some skins as the name
    # of the current section.
    xbmcplugin.setPluginCategory(_HANDLE, category)
    # Set plugin content. It allows Kodi to select appropriate views
    # for this type of content.
    xbmcplugin.setContent(_HANDLE, 'videos')
    # Get the list of videos in the category.
    videos = get_videos(category)
    # Iterate through videos.
    for video in videos:
        # Create a list item with a text label and a thumbnail image.
        list_item = xbmcgui.ListItem(label=video['name'])
        # Set additional info for the list item.
        # 'mediatype' is needed for skin to display info for this ListItem correctly.
        list_item.setInfo('video', {'title': video['name'],
                                    'genre': video['genre'],
                                    'mediatype': 'video'})
        # Set graphics (thumbnail, fanart, banner, poster, landscape etc.) for the list item.
        # Here we use the same image for all items for simplicity's sake.
        # In a real-life plugin you need to set each image accordingly.
        list_item.setArt({'thumb': video['thumb'], 'icon': video['thumb'], 'fanart': video['thumb']})
        # Set 'IsPlayable' property to 'true'.
        # This is mandatory for playable items!
        list_item.setProperty('IsPlayable', 'true')
        # Create a URL for a plugin recursive call.
        # Example: plugin://plugin.video.example/?action=play&video=http://www.vidsplay.com/wp-content/uploads/2017/04/crab.mp4
        url = get_url(action='play', video=video['video'])
        # Add the list item to a virtual Kodi folder.
        # is_folder = False means that this item won't open any sub-list.
        is_folder = False
        # Add our item to the Kodi virtual folder listing.
        xbmcplugin.addDirectoryItem(_HANDLE, url, list_item, is_folder)
    # Add a sort method for the virtual folder items (alphabetically, ignore articles)
    xbmcplugin.addSortMethod(_HANDLE, xbmcplugin.SORT_METHOD_LABEL_IGNORE_THE)
    # Finish creating a virtual folder.
    xbmcplugin.endOfDirectory(_HANDLE)


def play_video(path):
    """
    Play a video by the provided path.

    :param path: Fully-qualified video URL
    :type path: str
    """
    # Create a playable item with a path to play.
    play_item = xbmcgui.ListItem(path=path)
    # Pass the item to the Kodi player.
    xbmcplugin.setResolvedUrl(_HANDLE, True, listitem=play_item)


def router(paramstring):
    """
    Router function that calls other functions
    depending on the provided paramstring

    :param paramstring: URL encoded plugin paramstring
    :type paramstring: str
    """
    # Parse a URL-encoded paramstring to the dictionary of
    # {<parameter>: <value>} elements
    params = dict(parse_qsl(paramstring))
    # Check the parameters passed to the plugin
    if params:
        if params['action'] == 'listing':
            # Display the list of videos in a provided category.
            list_videos(params['category'])
        elif params['action'] == 'play':
            # Play a video from a provided URL.
            play_video(params['video'])
        else:
            # If the provided paramstring does not contain a supported action
            # we raise an exception. This helps to catch coding errors,
            # e.g. typos in action names.
            raise ValueError('Invalid paramstring: {}!'.format(paramstring))
    else:
        # If the plugin is called from Kodi UI without any parameters,
        # display the list of video categories
        list_categories()


if __name__ == '__main__':
    # Call the router function and pass the plugin call parameters to it.
    # We use string slicing to trim the leading '?' from the plugin call paramstring
    router(sys.argv[2][1:])
