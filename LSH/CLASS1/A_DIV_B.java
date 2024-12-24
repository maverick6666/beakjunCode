package Class_1;
import java.util.Scanner;

class A_DIV_B {
	public static void main(String[] args){
		
	    System.out.println("두 숫자 a,b를 입력하세요 (단, 0<A, B<10): ");
	    Scanner scanner = new Scanner(System.in);
	    
	    double a = scanner.nextDouble();
	    double b = scanner.nextDouble();
	    if (0<a && b<10) {
	    	double div = a/b;
	    	System.out.println("결과는"+div+"입니다.");
	    
	    }else {
	    	System.out.println("입력 값이 맞지 않습니다.");
	    }
	    	
	    	
	    
	    }
	 
	}


