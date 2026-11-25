from pyrevit import DB


class RoomServices:
    def __init__(self):
        pass

    def get_room_in_level(self, level):
        """
        Get all rooms in a specific level.

        :param level: The level element.
        :return: A list of room elements.
        """
        collector = DB.FilteredElementCollector(level.Document)
        rooms = (
            collector.OfCategory(DB.BuiltInCategory.OST_Rooms)
            .WhereElementIsNotElementType()
            .ToElements()
        )
        rooms_in_level = [room for room in rooms if room.LevelId == level.Id]
        return rooms_in_level

    def get_room_boudary(self, room):
        """
        Get the boundary of a room.

        :param room: The room element.
        :return: A list of boundary curves.
        """
        options = DB.SpatialElementBoundaryOptions()
        boundaries = room.GetBoundarySegments(options)
        boundary_curves = []
        for boundary in boundaries:
            for segment in boundary:
                boundary_curves.append(segment.GetCurve())
        return boundary_curves
