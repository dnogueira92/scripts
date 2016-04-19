<!DOCTYPE html>
<html>
  <head>

  </head>
  <body>

%list = []
%NoRes = str("No reservations in the system")


<center>
<iframe src="https://calendar.google.com/calendar/embed?showTitle=0&amp;height=600&amp;wkst=1&amp;bgcolor=%23FFFFFF&amp;src=dnogueira%40intranet.techsquare.com&amp;color=%231B887A&amp;ctz=America%2FNew_York" style="border-width:0" width="800" height="600" frameborder="0" scrolling="no"></iframe>
</center>

<br><br><br>

%if(reservation.startswith("No")):
{{reservation}}
%else:
<table border="1"">
<tr>
<th>Reservation Name</th>
<th>Information</th>
</tr>
%	res = reservation.split()
%	for item in res:
%   		key, val = item.split("=")


		%if key == "ReservationName":
%			resname = val
%			list = []
<tr>
<td>{{resname}}</td>
		%elif (key == "StartTime") or (key == "EndTime") or (key == "Nodes") or (key == "Users") or (key == "State"):
%			list.append(key + ": " + val)

%if (key == "State") and (val == "ACTIVE"):
<td>
<font color=#FF0000>

%	for item in list:
	{{item}} | 

%end
</font>
</td>
%elif (key == "State"):
<td>
<font color=#005600>

%	for item in list:
	{{item}} | 

%end
</font>
</td>
%end
%end
%end
</tr>			
</table>
%end



  </body>
</html>
