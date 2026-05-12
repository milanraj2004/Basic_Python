
class Milan:
    def __init__(self,type_,strength):

        self.type_ = type_
        self.strength = strength


# class Delhi(Milan):
#     def __init__(self, type_, strength, level):
#         self.type_ = type_
#         self.strength = strength
#         self.level = level


# class Delhi(Milan):
#     def __init__(self, type_, strength, level):
#         Milan.__init__(self, type_, strength)
#         self.level = level
#


class Delhi(Milan):
    def __init__(self, type_, strength, level):
        super().__init__(type_, strength)
        self.level = level


       