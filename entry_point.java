import py4j.GatewayServer;

public class entry_point {

    private order_manager_support order_manager;

    public entry_point() {
        order_manager = new order_manager_support();
        order_manager.get_work_time();
    }

    public order_manager_support getStack() {
        return order_manager;
    }

    public static void main(String[] args) {
        GatewayServer gatewayServer = new GatewayServer(new entry_point());
        gatewayServer.start();
        System.out.println("Gateway Server Started");
    }

}