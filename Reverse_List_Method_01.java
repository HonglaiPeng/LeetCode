class Solution {
    public ListNode reverseList(ListNode head) {
        if(head == null)
            return head;
        // Method 1: Create new list
        
        // build dummy node
        ListNode dummy = head;
        int len = 0;
        while(dummy != null){
            len++;
            dummy = dummy.next;
        }
        // build array to store the values of list
        int[] arr = new int[len];
        int i = 0;
        while(head != null){
            arr[i] = head.val;
            head = head.next;
            i++;
        }
      
        ListNode newHead = new ListNode(arr[len - 1]);
        ListNode newDummy = newHead;
        int j = len - 2;
        while(j >= 0){
            newDummy.next = new ListNode(arr[j]);
            j--;
            newDummy = newDummy.next;
        }
        return newHead;
    }
}