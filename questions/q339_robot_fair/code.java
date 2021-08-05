import java.io.*;
import java.util.*;
class robotAtTheFair {
	public static void main(String [] args) {
	    int r,c,i,j,x,y,n,m,s=0,dir=1,direction=1;
	    Scanner sc = new Scanner(System.in);
	    r = sc.nextInt();
	    c = sc.nextInt();
	    char gnd[][] = new char[r][c];
	    for(i=0;i<r;i++)
	    {
	        for(j=0;j<c;j++)
	        {
	        	gnd[i][j] = sc.next().charAt(0);
	        }
	    }
	    x = sc.nextInt();
	    y = sc.nextInt();
	    n = sc.nextInt();
	    char path[] = new char[n];
	    path = sc.next().toCharArray();
	  /*  String a = sc.next(); 
	    for(i=0;i<n;i++)
	    {
	    	path[i] = a.charAt(i);
	    }*/
	    for(direction=1;direction<5;direction++)
	    {
	        dir=direction;
	        i=x;j=y;
	        for(m=0;m<n;m++)
	        {
	            if(dir==1)                            //North
	            {
	                switch(path[m])
	                {
	                    case 'F':if(i>0){i--;}else{s=-1;}break;
	                    case 'L':dir=4;break;
	                    case 'R':dir=2;break;
	                }
	            }
	            else if(dir==2)                       //East
	            {
	                switch(path[m])
	                {
	                    case('F'):if(j<c-1) {
	                    	j++;
	                    }
	                    else {
	                    	s=-1;
	                    	break;
	                    }
	                    case('L'):dir=1;break;
	                    case('R'):dir=3;break;
	                }
	            }
	            else if(dir==4)                       //West
	            {
	                switch(path[m])
	                {
	                    case('F'):if(j>0) {
	                    	j--;
	                    }
	                    else {
	                    	s=-1;
	                    	break;
	                    }
	                    case('L'):dir=3;break;
	                    case('R'):dir=1;break;
	                }
	            }
	            else if(dir==3)                                       //South
	            {
	                switch(path[m])
	                {
	                    case('F'):if(i<r-1) {
	                    	i++;
	                    }
	                    else {
	                    	s = -1;
	                    	break;
	                    }
	                    case('L'):dir=2;break;
	                    case('R'):dir=4;break;
	                }
	            }
	            if((gnd[i][j]=='X')||(s==-1)){s=-1;break;}
	        }
	    if(s==0){gnd[i][j]='o';}
	    s=0;
	    }
	    for(i=0;i<r;i++)
	    {
	        for(j=0;j<c;j++)
	        {
	            if(gnd[i][j]=='o') {
	            	System.out.print(i+" ");
	            	System.out.print(j);
	            	System.out.println();
	            	}
	        }
	    }

	}
}
