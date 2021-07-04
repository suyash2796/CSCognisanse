public class SinglyLinkList {

	Node head;
	
	static class Node{
		private int value;
		private Node next;
		
		public Node(int val) {
			// TODO Auto-generated constructor stub
			this.value=val;
		}
		public int getValue() {
			return value;
		}

		public void setValue(int value) {
			this.value = value;
		}


		public Node getNext() {
			return next;
		}


		public void setNext(Node next) {
			this.next = next;
		}

	}
	
	public void removeLast(SinglyLinkList s) {
		
		Node prev = s.head;
		Node last = s.head.next;
		while(last.getNext()!=null) {
			prev = last;
			last = last.getNext();
		}
		prev.setNext(null);
	}
	
	public void removeByValue(SinglyLinkList s,int val) {
		if(s.head==null) {
			return;
		}
		if(s.head.getNext() == null ) {
			if( head.getValue()==val)
				head=null;
			return;
		}else {
			if( head.getValue()==val) {
				head=head.getNext();
				return;
			}
		}
		
		Node n = s.head.getNext();
		Node prev = s.head;
		Node next = n.getNext();
		
		while(n.getNext()!=null) {
			
			if(n.getValue()==val) {
				prev.setNext(next);
				return;
			}
			prev=n;
			n = n.getNext();
			next = n.getNext();
		}
		if(n.getValue()==val)
			prev.setNext(null);
		
	}
	public void printList(SinglyLinkList s) {
		if(s.head==null)
			return;
		Node n = s.head;
		while(n.getNext()!=null) {
			System.out.println(n.getValue());
			n = n.getNext();
		}
		System.out.println(n.getValue());
		System.out.println("*****************");
	}
	
	public SinglyLinkList addtoList(SinglyLinkList s , int val) {
		
		Node n = new Node(val);
		
		if(s.head != null) {
			Node last = s.head;
			while(last.getNext()!=null) {
				last = last.getNext();
			}
			last.setNext(n);
		}else
			s.head = n;
		
		return s;
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		SinglyLinkList s = new SinglyLinkList();
		s.removeByValue(s, 0);//Empty linked list
		s.printList(s);
		s.addtoList(s, 1);//Insertion
		s.removeByValue(s, 1);//Single Element 
		s.printList(s);
		s.addtoList(s, 2);
		s.addtoList(s, 3);
		s.addtoList(s, 4);
		s.addtoList(s, 5);
		s.printList(s);
		s.removeLast(s);//Remove last element
		s.printList(s);
		s.removeByValue(s, 2);//remove element by value
		s.printList(s);
	}

}
