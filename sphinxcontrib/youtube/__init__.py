from  . import youtube, vimeo, msstream

def setup(app):
    app.add_node(youtube.youtube, **youtube._NODE_VISITORS)
    app.add_directive("youtube", youtube.YouTube)
    app.add_node(vimeo.vimeo, **vimeo._NODE_VISITORS)
    app.add_directive("vimeo", vimeo.Vimeo)
    app.add_node(msstream.msstream, **msstream._NODE_VISITORS)
    app.add_directive("msstream", msstream.Msstream)
