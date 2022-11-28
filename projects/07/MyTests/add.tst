load add.asm,
output-file add.out,
compare-to add.cmp,
output-list RAM[0]%D2.6.2 RAM[256]%D2.6.2 RAM[257]%D2.6.2;

repeat 30 {
  ticktock;
}
output;
