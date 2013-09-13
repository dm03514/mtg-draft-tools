mtg-draft-tools
===============

mtg-draft-tools allows the easy creation of pack, draft pool, and sealed deck's.


The idea is to make it simple to generate packs from Magic Work Station (MWS) expansion files.

Once packs can be generated, sealed pools can be easily generated.

Look in `bin` for a list of commands available.

Right now there is only a command to generate homogonous sealed pools (same pack pools)

To generate a sealed pool for m2014:

    cd mtgdrafttools
    python bin/generate_sealed.py m14


Or for RTR block (2 packs of each expansion):

    cd mtgdrafttools
    python bin/generate_sealed.py m14
