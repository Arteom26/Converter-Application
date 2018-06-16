package latest;

import java.awt.FlowLayout;

import javax.swing.JFrame;

@SuppressWarnings("serial")
public class StartPage extends JFrame{
	public StartPage() {
		setSize(300, 200);
		setLayout(new FlowLayout());
		setDefaultCloseOperation(EXIT_ON_CLOSE);
		
		setVisible(true);
	}
}
