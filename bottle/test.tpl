<!DOCTYPE html>
<html>
  <head>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css"/>
  </head>
  <body>

%list = []

<table border="1"">
<tr>
<th>Reservation Name</th>
<th>Information</th>
</tr>
%	for item in res:
%   		key, val = item.split("=")


		%if key == "ReservationName":
%			resname = val
%			list = []
<tr>
<td>{{resname}}</td>
		%else:
%			list.append(key + "= " + val)

%if key == "State":
<td>
%	for item in list:
	{{item}}<br>
%end
</td>
%end
%end
%end
</tr>			
</table>

<br>
<br>
<br>
<center>
<iframe src="https://calendar.google.com/calendar/embed?showTitle=0&amp;height=600&amp;wkst=1&amp;bgcolor=%23FFFFFF&amp;src=dnogueira%40intranet.techsquare.com&amp;color=%231B887A&amp;ctz=America%2FNew_York" style="border-width:0" width="800" height="600" frameborder="0" scrolling="no"></iframe>
</center>



  </body>
</html>
