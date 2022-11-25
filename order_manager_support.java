


public class order_manager_support
{
    public  order_manager_support(){}
    public static void main(String[] arg) 
    {
        order_manager_support myObject = new order_manager_support();
        String[] free_time = myObject.get_work_time();
        for (int i = 0; i < free_time.length; i++) {
            System.out.println(free_time[i]);
        }
    }
  
    public double str_to_floattime(String time)
    {
        if (time.charAt(1) == ':')
        {
            return Double.parseDouble(Character.toString(time.charAt(0)))+Double.parseDouble(Character.toString(time.charAt(2))+Character.toString(time.charAt(3)))/60;
        }
        else
        {
            return Double.parseDouble(Character.toString(time.charAt(0))+ Character.toString(time.charAt(1)))+Double.parseDouble(Character.toString(time.charAt(3))+Character.toString(time.charAt(4)))/60;
        }
    }

    public String floattime_to_str(double time)
    {
        String hours = String.valueOf((int)time);
        String mins = String.valueOf(time % 1 / 5 * 3);
        mins = Character.toString(mins.charAt(2)) + "0";
        return hours + ":" + mins;
    }

    public String[] get_work_time()
    {
        String[] free_time = new String[28];
        for (int i = 0; i < free_time.length; i++) {
            free_time[i] = floattime_to_str(8 + i*0.5);
        }
        return free_time;
    }
    public String[] get_free_table_time(String table)
    {
        String[] free_time = new String[28];
        return free_time;
        /*
        def get_free_table_time(table):
    open_time = "08:00"
    close_time = "22:00"
    ordet_time_delta = "04:00"
    free_time = []
    ordered_start_time = []
    events = collect_data()
    for event in events:
        #print(event)
        if (event.get("title") == table): ordered_start_time.append(event.get("start_time"))
    time = str_to_floattime(open_time)
    while (time < str_to_floattime(close_time)):
        flag = 0
        for t in ordered_start_time:
            if (time+str_to_floattime(ordet_time_delta) > str_to_floattime(t)) and (time < str_to_floattime(t)+str_to_floattime(ordet_time_delta)):
                flag = 1
        if (flag == 0): 
            free_time.append(floattime_to_str(time))
        time += 0.5
    
    return free_time

def get_free_table_time_var(table):
    events = collect_data()
    order_time = []
    
    for event in events:
        #print(event)
        if (event.get("title") == table): 
            order_time.append(event.get("start_time"))
            for t in range(1,8):
                order_time.append(floattime_to_str(str_to_floattime(event.get("start_time"))+0.5*t))
                order_time.append(floattime_to_str(str_to_floattime(event.get("start_time"))-0.5*t))
    return sorted(list(set(work_time) - set(order_time)))
         */
    }
}