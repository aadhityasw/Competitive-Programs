public class Solution {
	public int power(String a)
	{
		if(a==null)
			return 0;
		char arr[] = a.toCharArray();
		
		//System.out.println(arr);
		int arrStart=0;
		int arrEnd=arr.length-1;
		
		while(arrStart<arrEnd)
		{
			
			if(((int)arr[arrEnd]-48)%2!=0)
				return 0;
			for(int i=arrStart, carryOver=0;i<=arrEnd;i++)
			{
				int currElement = (int)arr[i]-48;
				currElement=10*carryOver+currElement;
				
				if(currElement<2)
				{
					arr[i]=48;
					carryOver=currElement;
				}
				
				else
				{
					arr[i]=(char)(48 + currElement/2);
					carryOver=currElement%2;
				}
				//System.out.println(arr);
			}
			
			if(arr[arrStart]==48)
				arrStart++;
		}
		if(((int)arr[arrEnd]-48)%2==0)
			return 1;
		return 0;
    }
}
