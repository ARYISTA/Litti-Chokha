class BusBooking:

    def __init__(self, n: int):
        
        self.booked_seats = {}
        
        
        self.row_state = {} 
        
        self.total_time = 0

    def toggle(self, seat: str) -> None:
        letter = seat[0]
        row = int(seat[1:])
        
        if row not in self.row_state:
            self.row_state[row] = {'A': False, 'B': False, 'C': False, 'D': False}
            
        # Case 1: Seat is currently booked -> FREE IT
        if seat in self.booked_seats:
            cost = self.booked_seats.pop(seat)
            self.total_time -= cost
            self.row_state[row][letter] = False
            
        
        else:
            cost = 1
            if letter == 'A' and self.row_state[row]['B']:
                cost = 3
            elif letter == 'D' and self.row_state[row]['C']:
                cost = 3
                
            self.booked_seats[seat] = cost
            self.total_time += cost
            self.row_state[row][letter] = True

    def getTotalTime(self) -> int:
        return self.total_time

    def getMinTime(self) -> int:
       
        return len(self.booked_seats)