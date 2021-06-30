public class MissingNumber{

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int arr[] = {1,2,3,4,5,6,8};
		int size = arr.length+1;
		int nSum = size	*(size+1)/2;
		int arrSum = 0;
		for(int i : arr) {
			arrSum+=i;
		}
		System.out.println(nSum-arrSum);
		
	}

}