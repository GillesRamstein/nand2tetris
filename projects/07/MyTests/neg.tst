load neg.asm,
output-file neg.out,
compare-to neg.cmp,
output-list RAM[0]%D2.6.2 RAM[256]%D2.6.2;

repeat 30 {
  ticktock;
}
output;
