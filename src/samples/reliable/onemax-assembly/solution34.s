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
    and %ecx, %eax
    jno n13
    shr $188, %ebx
    jne n17
    jne n18
    sub %edx, %ecx
    shl $100, %ebx
    jnz n12
n12:
    or %eax, %ebx
n13:
    shl $4, %ecx
    shr $192, %ecx
    add %ebx, %ebx
n16:
    or %edx, %eax
n17:
    sub %ecx, %eax
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
