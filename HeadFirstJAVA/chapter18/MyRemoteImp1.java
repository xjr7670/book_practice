import java.rmi.server.UnicastRemoteObject;
import java.rmi.RemoteException;
import java.rmi.Naming;

public class MyRemoteImp1 extends UnicastRemoteObject implements MyRemote {
    public String sayHello() {
        return "Server says, 'Hey'";
    }

    public MyRemoteImp1() throws RemoteException {}

    public static void main(String[] args) {
        try {
            MyRemote service = new MyRemoteImp1();
            Naming.rebind("Remote Hello", service);
        } catch (Exception ex) {
            ex.printStackTrace();
        }
    }
}