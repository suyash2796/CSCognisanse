public class MonotonicArray {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] arr = {1,2,3,4,7,9,10};
		int prev = arr[0];
		int i=0;
		int j=0;
		for (int a :arr) {
			System.out.println("a "+a);
			if(a>=prev) 
				i++;
			
			if(a<=prev)
				j++;
			System.out.println("j:i:prev "+j+":"+i+":"+prev);
			prev=a;
		}
		
		if(i==arr.length || j==arr.length) {
			System.out.println("Monotonic Array");
		}else
			System.out.println("Non-Monotonic Array");
	}

}