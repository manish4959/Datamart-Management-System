import java.io.*;
import javax.servlet.*;
import javax.servlet.http.*;
import java.sql.*;
public class AddItemController extends HttpServlet {
public void doPost(HttpServletRequest req,HttpServletResponse resp)throws ServletException,IOException
{
resp.setContentType("text/html"); PrintWriter out=resp.getWriter();
String name=req.getParameter("Name"); 
   System.out.println(name); doubleunitcost=Double.parseDouble(req.getParameter("ItemCost")); System.out.println(unitcost);
try
{
Class.forName("sun.jdbc.odbc.JdbcOdbcDriver");
Connection con=DriverManager.getConnection("jdbc:odbc:dmms","dmms","dmms");
//Connection //con=DriverManager.getConnection("jdbc:odbc:sai","scott","tiger");
Statement stmt=con.createStatement();
int ITEMID=0;
ResultSet rs=stmt.executeQuery("select max(ITEMID) from item"); if(rs.next())
{
ITEMID=rs.getInt(1); 
 
   values(?,?,?)");
ITEMID++;
System.out.println("id"+ITEMID); }
else {
ITEMID=1; }
PreparedStatement pstmt=con.prepareStatement("insert into item
System.out.println("pstmt"); pstmt.setInt(1,ITEMID); pstmt.setString(2,name); pstmt.setDouble(3,unitcost); int i=pstmt.executeUpdate(); if(i==1)
{
out.println("Data Register");

 
   resp.setHeader("Refresh","2;URL=./chooseitem.html");
} else
{
out.println("Data not Register "); resp.setHeader("Refresh","2;URL=./chooseitem.html");
}
rs.close(); pstmt.close(); stmt.close(); con.close();
}catch(Exception e) {
System.out.println(e); }

 
   }
import java.io.*;
import javax.servlet.*;
import javax.servlet.http.*;
import java.sql.*;
public class AddSubLocRetailer extends HttpServlet {
public void doPost(HttpServletRequest req,HttpServletResponse resp)throws ServletException,IOException
{
resp.setContentType("text/html");
PrintWriter out=resp.getWriter();
String cpass=req.getParameter("Cpassword");
String name=req.getParameter("Name"); String house=req.getParameter("House"); String street=req.getParameter("Street"); String city=req.getParameter("City");

 
   String state=req.getParameter("State"); String country=req.getParameter("Country"); String phone=req.getParameter("Phone"); String email=req.getParameter("Email");
try {
Class.forName("sun.jdbc.odbc.JdbcOdbcDriver");
Connection con=DriverManager.getConnection("jdbc:odbc:dmms","dmms","dmms");
//Class.forName("sun.jdbc.odbc.JdbcOdbcDriver");
//Connection //con=DriverManager.getConnection("jdbc:odbc:sai","scott","tiger");
Statement stmt=con.createStatement(); int RETAILERID=0;

 
   ResultSet rs=stmt.executeQuery("select max(RETAILERID) from retailer"); System.out.println("rs");
if(rs.next())
{
RETAILERID=rs.getInt(1); RETAILERID++;
System.out.println("id"+RETAILERID); }
else {
RETAILERID=1; }
PreparedStatement pstmt=con.prepareStatement("insert into retailer values(?,?,?,?,?,?,?,?,?,?)");
System.out.println("pstmt"); 
 
   //pstmt.setInt(1,subinchargeid);
pstmt.setInt(1,RETAILERID);
pstmt.setString(2,cpass);
pstmt.setString(3,name);
pstmt.setString(4,house);
pstmt.setString(5,street);
pstmt.setString(6,city);
pstmt.setString(7,state);
pstmt.setString(8,country);
 
   pstmt.setString(9,phone);
pstmt.setString(10,email);
int i=pstmt.executeUpdate(); System.out.println("record inserted"); if(i==1)
{
out.println("Data Register");
out.println("your id is "+RETAILERID); resp.setHeader("Refresh","2;URL=./blank.html");
} else
{
out.println("Data not Register ");
 
} }
   resp.setHeader("Refresh","2;URL=./AddSubLocRetailer"); }
rs.close(); pstmt.close(); stmt.close(); con.close();
}catch(Exception e) {
System.out.println(e); 
}
                                             }
                                             }
                                             
