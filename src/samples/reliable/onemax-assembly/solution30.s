    .file   "solution.c"
    .text
    .globl  _darwin
    .def    _darwin;        .scl    2;      .type   32;     .endef
_darwin:
LFB17:
    .cfi_startproc
    pushl   %ebp
    .cfi_def_cfa_offset 8
    .cfi_offset 5, -8
    movl    %esp, %ebp
    .cfi_def_cfa_register 5

    movl	$-28251, %eax
    movl	$24706, %ebx
    movl	$-2288, %ecx
    movl	$23988, %edx

    jne n16
    shl $167, %eax
    jno n13
    add %ecx, %ebx
    jne n17
    jne n18
    shr $237, %ecx
    xor %edx, %ebx
    jno n18
    shr $77, %eax
n13:
    or %eax, %ebx
    xor %ecx, %eax
    shl $0, %edx
n16:
    shl $53, %ebx
n17:
    shr $214, %edx
n18:
    movl	%eax, -4(%ebp)
    movl	-4(%ebp), %eax
    leave
    .cfi_restore 5
    .cfi_def_cfa 4, 4
    ret
    .cfi_endproc
LFE17:
   .ident  "GCC: (MinGW.org GCC-8.2.0-5) 8.2.0"
