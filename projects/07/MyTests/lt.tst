load lt.asm,
output-file lt.out,
compare-to lt.cmp,
output-list RAM[0]%D2.6.2 RAM[256]%D2.6.2 RAM[257]%D2.6.2 RAM[258]%D2.6.2 RAM[259]%D2.6.2;

repeat 100 {
  ticktock;
}
output;
