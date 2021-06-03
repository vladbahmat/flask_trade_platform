from trade_platform.models import Profile, WatchList

class WatchListService():
    @staticmethod
    def watchlist_autocreate(profile):
        data = {"profile": profile}
        WatchList(**data).insert()