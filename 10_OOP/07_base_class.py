class chai:
    def __init__(self,type_,strength):
        self.type=type_
        self.strenght=strength
        
# class GingerChai(chai):
#     def __init__(self, type_, strength,spice_level):
#         self.type=type_
#         self.strenght=strength
#         self.spice_level=spice_level

# class GingerChai(chai):
#     def __init__(self, type_, strength,spice_level):
#         chai.__init__(self,type_,strength)
#         self.spice_level=spice_level
        
class GingerChai(chai):
    def __init__(self, type_, strength,spice_level):
        super().__init__(type_, strength)
        self.spice_level=spice_level

