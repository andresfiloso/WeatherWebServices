package dao;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.TimeZone;

public class DataSource {

	private Connection con;

	public DataSource() {

	}

	public ResultSet execute(String query) {
		ResultSet rs = null;
		this.open();

		try {
			Statement st = this.con.createStatement();
			rs = st.executeQuery(query);
		} catch (SQLException e) {
			e.printStackTrace();
		}

		return rs;
	}
	
	public int update(String query) {
		int rs = 0;
		this.open();

		try {
			Statement st = this.con.createStatement();
			rs = st.executeUpdate(query);
		} catch (SQLException e) {
			e.printStackTrace();
		}

		return rs;
	}

	private void open() {
		if (con == null) {
			try {
				//Class.forName("sun.jdbc.odbc.JdbcOdbcDriver");
				TimeZone timeZone = TimeZone.getTimeZone("UTC");
			    TimeZone.setDefault(timeZone);
				Class.forName("com.mysql.cj.jdbc.Driver");
				con = DriverManager.getConnection("jdbc:mysql://localhost/bdapiclima?serverTimezone=UTC", "root", "root");
			} catch (ClassNotFoundException e) {
				e.printStackTrace();
			} catch (SQLException e) {
				e.printStackTrace();
			}
		}
	}

	public void close() {
		if (con != null) {
			try {
				con.close();
				con = null;
			} catch (SQLException e) {
				e.printStackTrace();
			}
		}
	}
}
