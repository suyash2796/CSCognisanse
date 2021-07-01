import java.util.Arrays;

//find the pair of integer in an array whose sum is equal to given number
//Sliding window 
public class PairSum {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] arr = {1,2,3,4,5};
		Arrays.sort(arr);
		int totalSum=8,sum=0;
		int a = 0;
		int b = arr.length-1;
		while(true) {
			
			sum = arr[a]+arr[b];
			if(sum>totalSum)
				b--;
			else if (sum<totalSum)
				a++;
			else {
				System.out.println("The pair is "+arr[a]+" and "+arr[b]);
				break;
			}
		}
	}


}
