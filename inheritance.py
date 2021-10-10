class car:
    def __carno(self, no):
        self.no = no;
    def sits(self, seats_no):
        self.seats_no = seats_no;
        print(seats_no);
    def _color(self, colo):
        self.colo = colo;
        print(colo);
class maruti(car):
    def carcolor(self):
        print("pink");

m = maruti();
m.sits(3);
m._color("red");
m.__carno(123);