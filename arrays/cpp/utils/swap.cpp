/* Function to swap *a and *b */
// we have that function in STL but its better to have it handy
void swap(int *a, int *b)
{

 int temp = *a;
    *a = *b;
    *b = temp;
}