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

    movl	$-25209, %eax
    movl	$24709, %ebx
    movl	$30828, %ecx
    movl	$-15650, %edx

    jnz n13
    jne n5
n5:
    shr $222, %ecx
    jc n13
    xor %eax, %eax
    xor %ebx, %ebx
    add %edx, %eax
    jno n14
    and %edx, %eax
    cmp %ecx, %ecx
n13:
    shr $153, %ecx
n14:
    shl $167, %edx
    cmp %ecx, %ebx
    shr $215, %edx
    shl $160, %edx
    movl	%eax, -4(%ebp)
    movl	-4(%ebp), %eax
    leave
    .cfi_restore 5
    .cfi_def_cfa 4, 4
    ret
    .cfi_endproc
LFE17:
   .ident  "GCC: (MinGW.org GCC-8.2.0-5) 8.2.0"
